import pytest
from py_backwards.transformers.async_await import AsyncAwaitTransformer


@pytest.mark.parametrize('before, after', [
    ('''
async def fn():
    await range(10)
    ''', '''
@asyncio.coroutine
def fn():
    yield from range(10)
'''),
    ('''
async def fn():
    a = await range(10)
    ''', '''
@asyncio.coroutine
def fn():
    a = yield from range(10)
'''),
])
def test_transform(transform, ast, before, after):
    code = transform(AsyncAwaitTransformer, before)
    assert ast(code) == ast(after)
