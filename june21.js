const tasks = ["laundry", "shovel driveway", "grocery shopping", "check email", "daydream", "phone parents", "fill prescription", "exercise", "take out recycling", "check the weather"];
// for(let i = 0; i < tasks.length; i++) {
  //   console.log(i);
  // }
  
  
console.log("Sunday To Do List:");
tasks.forEach((task, index) => {
  console.log(`${index + 1}: ${task}`)
}) 