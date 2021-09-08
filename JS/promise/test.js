const p = new Promise((res, rej) => {
  res("123");
});
console.dir(p);

p.then(
  () => {
    console.log("sucess");
  },
  () => {
    console.log("fail");
  }
);
console.log(p);
