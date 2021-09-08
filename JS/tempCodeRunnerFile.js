function test() {
  let address = "nyc";
  return address;
}
function A() {
  let newAddress = test();
  return newAddress;
}
B = A();

console.log(B);
