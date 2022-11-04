print("Hello world!!")


def helloworld():
    hello = "Hello World!!"
    print(f"{hello}")
    hello2 = "hello2"
    print(f"{hello2}")


param_grid = {
    "penalty": ["l2", "l1", "elasticnet", "none"],
    "C": [0.001, 0.01, 0.1, 1, 2, 3, 4, 5, 10],
    "max_iter": [10000],
    "n_jobs": [-1],
}
