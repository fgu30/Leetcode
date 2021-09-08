// function helloWorld() {
//   let greeting = greeting || "Hello";
//   let name = name || "World";
//   return greeting + ", " + name + "!";
// }

let helloWorld = (greeting = "Hello", name = "World") =>
  greeting + " , " + name + "!";
console.log(helloWorld("nihao", "china"));
