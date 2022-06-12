import * as fs from 'fs';
const std: string = fs.readFileSync('/dev/stdin', 'utf8')

const chars = [...std]
chars.sort()

console.log(chars.join(''))