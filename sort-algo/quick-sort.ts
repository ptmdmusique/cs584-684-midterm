export const quickSort = (inputArr: number[]): number[] => {
  // if (inputArr.length < 2) {
  //   return inputArr;
  // }

  // const pivot = inputArr[0];
  // const left: number[] = [];
  // const right: number[] = [];

  // for (let i = 1; i < inputArr.length; i++) {
  //   const el = inputArr[i];
  //   el < pivot ? left.push(el) : right.push(el);
  // }

  // return [...quickSort(left), pivot, ...quickSort(right)];
  if (inputArr.length <= 1) return inputArr;
  let pp = Math.floor(inputArr.length / 2),
    pivot = inputArr[pp];
  const left = [],
    right = [];
  for (var i = 0; i < inputArr.length; i++) {
    if (i == pp) continue;
    if (inputArr[i] < pivot) {
      left.push(inputArr[i]);
    } else {
      right.push(inputArr[i]);
    }
  }
  return quickSort(left).concat(pivot, quickSort(right));
};

/**
 * Some notes:
 * 1. There is also the hidden complexity in spread operator
 */
