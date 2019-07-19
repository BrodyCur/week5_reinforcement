function longestConsecutive(words, num) {
  let uniqueWords = [...new Set(words)].sort((a, b) => {
    return b.length - a.length;
  });

  if (num > uniqueWords.length) {
    console.log(`${num} is more than the amount of unique words provided`);
  } else {
    console.log(uniqueWords.slice(0, num).join(""));
  }
}

longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3);
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2);