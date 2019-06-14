exampleArray = ["Totam", "ut", "odit","quis", "Maiores", "unde", "EX", "EST", "corporis"];


function myFunction(array) {
    for (i = 0; i < array.length; i ++) {
        if (array[i] == array[i].toLowerCase() && array[i].length > 4) {
            console.log('long and lowercase');
        } else if (array[i].length > 4) {
            console.log('long');
        } else if (array[i] == array[i].toLowerCase()) {
            console.log('lowercase');
        } else {
            console.log(array[i]);
        };
    };
}

myFunction(exampleArray);