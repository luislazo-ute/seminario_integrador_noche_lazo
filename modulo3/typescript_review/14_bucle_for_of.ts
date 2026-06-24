interface Item {
  nombre: string;
  precio: number;
  cantidad: number;
}

const carrito: Item[] = [
  { nombre: "Mouse",   precio: 25, cantidad: 2 },
  { nombre: "Teclado", precio: 80, cantidad: 1 },
  { nombre: "Monitor", precio: 200, cantidad: 3 },
];

let total = 0;
for (const item of carrito) {
  const subtotal = item.precio * item.cantidad;
  console.log(`${item.nombre}: $${subtotal}`);
  total += subtotal;
}
console.log(`TOTAL: $${total}`);  // TOTAL: $730



const temps = [22, 25, 28, 30, 27, 24];
let max = 0;
for (const temp of temps) {
  if (temp > max) {
    max = temp;
  }

}
console .log(max);