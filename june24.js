function strSum(str) {
  let numSum = 0;
  let array = str.split('');

  array.forEach(num => {
    numSum += +num;
  });
  return numSum
};

function luckCheck(str) {
  const left = str.slice(0, Math.floor(str.length / 2));
  const right = str.slice(Math.ceil(str.length / 2));

  if (str === '' || str.length <= 0 || (/^[A-Za-z]+$/.test(str))) {
    console.log('Erorr, invalid string. Gotta be a string of numbers my dude.')
  } else {
    console.log(strSum(left) === strSum(right));
  };
};

luckCheck('luck');
luckCheck('123456');
luckCheck('');
luckCheck('123123');
luckCheck('54463');
luckCheck('Helpmeplease');
luckCheck('0987654323456789');