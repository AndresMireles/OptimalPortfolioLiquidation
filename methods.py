import numpy as np

# Method for solving the system of q ODEs for w[q]
def solve_w_ODE(q_max, N, k, b, alpha, beta, gamma, eta, dt):
    """
    We solve backwards the systems of ODEs corresponding to w[q], which has the following expression (Preposition 1 from Guéant O., Lehalle CA., Fernandez Tapia J. (2012)):

        dw_q/dt = (alpha * q^2 - beta * q) * w_q(t) - eta * w_{q-1}(t)

    """

    # We create an array w with shape (q_max+1, len(time_grid) = N+1)
    w = np.zeros((q_max+1, N+1))

    # Boundary condition: for q=0, w[0,t] = 1 for all t
    w[0, :] = 1.0

    # Terminal condition: at t=T, for q>=1: w_q(T) = exp(-k*q*b)
    for q in range(1, q_max+1):
        w[q, -1] = np.exp(-k * q * b)

    # Now solve the ODE system backwards in time for q=1,...,q_max
    for t in range(N-1, -1, -1):
        # For each inventory level from 1 to q_max (note that this could be vectorized, but for clarity we will not do it)
        for q in range(1, q_max+1): # (w[0, :] is already fixed to 1)
            # Use the value at the next time step (i+1)
            derivative = (alpha * (q**2) - beta * q) * w[q, t+1] - eta * w[q-1, t+1]
            w[q, t] = w[q, t+1] - dt * derivative

    return w

# Method for computing the optimal quote delta[q] based on the system of w[q]
def compute_optimal_quote(q_max, N, k, b, alpha, beta, gamma, eta, dt):
    """
    We will use the following formula for the optimal quote (Theorem 1 from Guéant O., Lehalle CA., Fernandez Tapia J. (2012)):

        δa*(t,q) = 1/k * ln( w[q](t) / w[q-1](t) ) + 1/gamma * ln(1 + gamma/k)

    """
    w = solve_w_ODE(q_max,N,k,b,alpha,beta,gamma,eta,dt)

    optimal_quotes = np.zeros((q_max+1, N+1)) # we won't use index 0

    for q in range(1, q_max+1): # (this could also be vectorized)
        optimal_quotes[q] = (1/k) * np.log(w[q] / w[q-1]) + (1/gamma) * np.log(1 + gamma/k)

    return optimal_quotes

# Method to simulate market price, and given a list of quotes, keep track of the inventory
def simulate_trading_paths(M, N, dt, q_init, S_init, mu, sigma, k, gamma, quotes, A, b):
    """
    Simulate M trading paths with inventory, price, and cash.
    
    When a fill occurs (i.e. an order is executed), the cash is updated by adding the execution price:
      X_{t+dt} = X_t + (S_t + δa*(t,q)),
    where δa*(t,q) is the optimal quote for the current inventory q.
    
    At the end, the terminal profit and loss is given by:
      PnL = X_T + q_T*(S_T - b),
    with b being the penalty (or cost) for any remaining inventory.
    """
    q_max = quotes.shape[0] - 1  # maximum inventory level
    q_paths = np.empty((N+1, M), dtype=int)
    S_paths = np.empty((N+1, M))
    X_paths = np.empty((N+1, M))  # cash account
    
    # Initialize:
    q_paths[0, :] = q_init
    S_paths[0, :] = S_init
    X_paths[0, :] = 0.0  # set initial cash to zero
    
    for i in range(N):
        # Get current inventory for all paths
        current_q = q_paths[i, :].copy()
        # Boolean mask for active paths (inventory > 0)
        active = current_q > 0
        
        # For active paths, fetch the corresponding optimal quote
        current_quote = np.empty(M)
        current_quote[active] = quotes[current_q[active], i]
        current_quote[~active] = 0.0
        
        # Compute fill intensity and probability for active paths
        lam = A * np.exp(-k * current_quote)
        p_fill = lam * dt
        
        # Generate uniform random numbers and determine which active paths get a fill
        u = np.random.rand(M)
        fills = (u < p_fill) & active
        
        # Update inventory: subtract one unit for paths that got a fill
        new_q = current_q.copy()
        new_q[fills] -= 1
        q_paths[i+1, :] = new_q
        
        # Update cash:
        # For paths where a fill occurred, the cash increases by (S_t + current_quote)
        # For others, cash remains unchanged
        X_paths[i+1, :] = X_paths[i, :].copy()
        X_paths[i+1, fills] = X_paths[i, fills] + S_paths[i, fills] + current_quote[fills]
        
        # Update price using the Euler–Maruyama scheme
        dW = np.random.normal(0.0, np.sqrt(dt), M)
        S_paths[i+1, :] = S_paths[i, :] + mu * dt + sigma * dW

    # Final cash update: Liquidate any remaining inventory at S_T - b
    X_paths[-1, :] += q_paths[-1, :] * (S_paths[-1, :] - b)
        
    return q_paths, S_paths, X_paths