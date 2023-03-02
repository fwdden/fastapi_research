import asyncio
import logging
from rocketry import Rocketry
from rocketry.conds import every

# https://itnext.io/scheduler-with-an-api-rocketry-fastapi-a0f742278d5b
# https://github.com/Miksus/rocketry-with-fastapi

app = Rocketry(config={"task_execution": "async"})
logger = logging.getLogger("rocketry.task")
logger.addHandler(logging.StreamHandler())

# @app.task(every('10 seconds', based="finish"))
# async def do_permanently():
#     "This runs for really long time"
#     await asyncio.sleep(600000)

@app.task(every('2 seconds', based="finish"))
async def do_short():
    "This runs for short time"
    print('1')
    await asyncio.sleep(1)

# @app.task(every('20 seconds', based="finish"))
# async def do_long():
#     "This runs for long time"
#     await asyncio.sleep(60)

# @app.task(every('10 seconds', based="finish"))
# async def do_fail():
#     "This fails constantly"
#     await asyncio.sleep(10)
#     raise RuntimeError("Whoops!")

if __name__ == "__main__":
    # Run only Rocketry
    app.run()