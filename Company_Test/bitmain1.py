import random
import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_regression
import matplotlib.pyplot as plt
from scipy import stats
import pylab


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
            print("Converged, iterations: ", iter, "!!!")
            converged = True

        if iter == max_iter:
            print("Max iterations reached!!!")
            converged = True

    return theta0, theta1, J, iter


def gradient_descent_version2(alpha, X, Y, batch_size, tol=0.0001, max_iter=1000):
    # initialization
    theta = []
    J = []
    # number of samples
    n = len(X)
    # initial theta
    theta.append(np.ones(2))
    # initial total error J(n)
    J.append(0.5 * np.sum((Y - np.dot(X, theta))**2))

    # Iterate Loop
    converged = False
    iter = 0
    while not converged:
        iter += 1
        # generate the indexes for the batch sample
        subIndex = np.random.choice(range(n), batch_size)
        # generate the batch sample
        subX = [X[j] for j in subIndex]
        subY = [Y[j] for j in subIndex]
        # compute the gradient of batch cost J(m), where m<=n
        grad = np.dot(subX.transpose(), subY - np.dot(subX, theta))
        # update theta
        theta.append(theta - alpha * grad)
        # current totla error
        J.append(0.5 * np.sum((Y - np.dot(X, theta))**2))

        if (abs(J[-2] - J[-1]) <= tol):
            print("Converged, iterations: ", iter, "!!!")
            converged = True

        if iter == max_iter:
            print("Max iterations reached!!!")
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
    theta0, theta1, J, iter = gradient_descent_version1(
        alpha, X, Y, batch_size, tol, max_iter)
    # print results
    print("theta0 = {}\ttheta1 = {}".format(theta0[-1], theta1[-1]))
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(
        X[:, 0], Y)
    print("slope = {}\tintercept = {}".format(slope, intercept))

    # plot total cost
    plt.figure()
    plt.plot(range(iter+1), J)
    plt.xlabel('Iter')
    plt.title('Total Cost')
    # plot theta
    plt.figure()
    plt.plot(range(iter+1), theta0)
    plt.plot(range(iter+1), theta1)
    plt.xlabel('Iter')
    plt.title('Estimated Parameters')
    # plot original points and prediction
    plt.figure()
    Y_Predict = [theta0[-1]*X[i]+theta1[-1] for i in range(len(X))]
    plt.plot(X, Y, 'o')
    plt.plot(X, Y_Predict, 'k-')
    plt.show()
    