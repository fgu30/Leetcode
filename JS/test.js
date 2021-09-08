function test() {
  address = "nyc";
  return address;
}
function A() {
  newAddress = test();
  return newAddress;
}
B = A();

console.log(B);
