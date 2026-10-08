import dagster as dg


@dg.asset
def hello_world():
    print("Hello World from Dagster!")
    return "Hello World"


defs = dg.Definitions(
    assets=[hello_world],
)
