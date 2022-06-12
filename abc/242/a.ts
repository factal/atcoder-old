import * as fs from 'fs';
const std: string = fs.readFileSync('/dev/stdin', 'utf8')

const [a, b, c, x] = std.trim().split(' ').map(Number)

if (x <= a) {
  console.log(1.0)
}
else if (x <= b) {
  console.log(c / (b - a))
}
else {
  console.log(0)
}