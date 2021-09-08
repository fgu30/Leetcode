function UserException(message) {
  this.message = message;
  this.name = "UserException";
}
function fetchAddress() {
  let city = "NYC";
  return city;
}
function getMonthName(mo) {
  mo = mo - 1; // 调整月份数字到数组索引 (1=Jan, 12=Dec)
  var months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  if (months[mo] !== undefined) {
    return months[mo];
  } else {
    throw new UserException("InvalidMonthNo");
  }
}
const fetchAll = (mo) => {
  try {
    // statements to try
    // 15 超出边界并引发异常
    return getMonthName(mo);
  } catch (e) {
    let monthName = "unknown";
    console.log(e.message, e.name); // 传递异常对象到错误处理
  }
};

console.log(fetchAll(13));
