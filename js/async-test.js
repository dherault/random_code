async function foo() {
  return 'foo'
}

async function bar() {
  return await 'bar'
}

console.log('foo()', foo())
console.log('bar()', bar())
