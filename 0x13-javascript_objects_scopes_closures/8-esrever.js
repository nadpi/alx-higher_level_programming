#!/usr/bin/node
exports.esrever = function (list) {
  const arrRev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    arrRev.push(list[i]);
  }
  return arrRev;
};
