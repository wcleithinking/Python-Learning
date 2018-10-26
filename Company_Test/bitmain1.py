import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_regression
from scipy import stats
import matplotlib.pyplot as plt


def gradient_descent_version1(alpha, X, Y, batch_size, tol=0.0001, max_iter=1000):
    # initialization
    theta0 = []
    theta1 = []
    J = []
    # number of samples
    n = len(X)
    # initial theta
    theta0.append(np.random.random())
    theta1.append(np.random.random())
    # initial total error J(n)
    J.append(
        0.5 * sum([(Y[i] - theta0[-1]*X[i] - theta1[-1])**2 for i in range(n)]))

    # Iterate Loop
    converged = False
    iter = 0
    while not converged:
        iter += 1
        # generate the indexes for the batch sample
        subIndex = np.random.choice(range(n), batch_size)
        # compute the gradient of batch cost J(m), where m<=n
        grad0 = sum([(Y[j] - theta0[-1]*X[j] - theta1[-1])*(-X[j])
                     for j in subIndex])
        grad1 = sum([(Y[j] - theta0[-1]*X[j] - theta1[-1])*(-1)
                     for j in subIndex])
        # update theta
        theta0.append(theta0[-1] - alpha * grad0)
        theta1.append(theta1[-1] - alpha * grad1)
        # current totla error
        J.append(
            0.5 * sum([(Y[i] - theta0[-1]*X[i] - theta1[-1])**2 for i in range(n)]))

        if (abs(J[-2] - J[-1]) <= tol):
            print("Version   1: Converged, iterations: ", iter, "!!!")
            converged = True

        if iter == max_iter:
            print("Version   1: Max iterations reached!!!")
            converged = True

    return theta0, theta1, J, iter


def gradient_descent_version2(alpha, X, Y, batch_size, tol=0.0001, max_iter=1000):
    # initialization
    theta = []
    J = []
    # number of samples
    n = X.shape[0]
    # initial theta
    theta.append(np.ones(2))
    # initial total error J(n)
    J.append(0.5 * np.sum((Y - np.dot(X, theta[-1])**2)))

    # Iterate Loop
    converged = False
    iter = 0
    while not converged:
        iter += 1
        # generate the indexes for the batch sample
        subIndex = np.random.choice(range(n), batch_size)
        # generate the batch sample
        subX = np.array([X[j] for j in subIndex])
        subY = np.array([Y[j] for j in subIndex])
        # compute the gradient of batch cost J(m), where m<=n
        grad = np.dot(-subX.transpose(), subY - np.dot(subX, theta[-1]))
        # update theta
        theta.append(theta[-1] - alpha * grad)
        # current totla error
        J.append(0.5 * np.sum((Y - np.dot(X, theta[-1]))**2))

        if (abs(J[-2] - J[-1]) <= tol):
            print("Version   2: Converged, iterations: ", iter, "!!!")
            converged = True

        if iter == max_iter:
            print("Version   2: Max iterations reached!!!")
            converged = True
    return theta, J, iter


if __name__ == '__main__':
    # generate samples
    X, Y = make_regression(n_samples=100, n_features=1,
                           n_informative=1, random_state=0, noise=8)
    # set parameters
    alpha = 0.01    # learning rate
    batch_size = 50  # batch size
    tol = 0.01      # convergence criteria
    max_iter = 1000  # max iterations
    # calculate
    theta0, theta1, J_v1, iter_v1 = gradient_descent_version1(
        alpha, X, Y, batch_size, tol, max_iter)
    Xnew = np.c_[X, np.ones(X.shape[0])]
    theta, J_v2, iter_v2 = gradient_descent_version2(
        alpha, Xnew, Y, batch_size, tol, max_iter)
    # print results
    print("Version   1: theta0 = {}\t theta1 = {}".format(
        float(theta0[-1]), float(theta1[-1])))
    print("Version   2: theta0 = {}\t theta1 = {}".format(
        theta[-1][0], theta[-1][1]))
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(
        X[:, 0], Y)
    print("Scipy Stats: theta0 = {}\t theta1 = {}".format(slope, intercept))

    # plot total cost
    plt.figure()
    plt.plot(range(iter_v1+1), J_v1, linewidth=1, label='Version 1')
    plt.plot(range(iter_v2+1), J_v2, linewidth=2, label='Version 2')
    plt.legend()
    plt.xlabel('Iterations')
    plt.title('Total Cost')
    # plot theta
    plt.figure()
    plt.plot(range(iter_v1+1), theta0, color='blue',
             linewidth=1, label=r'$\hat{\theta}_0$ in Version 1')
    plt.plot(range(iter_v2+1), [subtheta[0] for subtheta in theta],
             color='yellow', linewidth=2, label=r'$\hat{\theta}_0$ in Version 2')
    plt.plot(range(iter_v1+1), theta1, color='green',
             linewidth=1, label=r'$\hat{\theta}_1$ in Version 1')
    plt.plot(range(iter_v2+1), [subtheta[1] for subtheta in theta],
             color='magenta', linewidth=2, label=r'$\hat{\theta}_1$ in Version 2')
    plt.legend()
    plt.xlabel('Iterations')
    plt.title('Estimated Parameters')
    # plot original points and prediction
    plt.figure()
    Y_Predict_v1 = [theta0[-1]*X[i]+theta1[-1] for i in range(len(X))]
    Y_Predict_v2 = [theta[-1][0]*X[i]+theta[-1][1] for i in range(len(X))]
    plt.plot(X, Y, 'o', label='Samples')
    plt.plot(X, Y_Predict_v1, 'b-', label='Version 1')
    plt.plot(X, Y_Predict_v2, 'y-', label='Version 2')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regression Results')

    # Show the figures
    plt.show()
