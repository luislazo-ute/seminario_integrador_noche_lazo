// null-undefined.ts

// En JS esto no da error, en TS sí (modo estricto)
// let nombreUnd: string = null;    // ❌ Error

// Para permitir null hay que declararlo explícitamente
let nombreUnd: string | null = null;   // ✅ puede ser string o null

nombreUnd = "Ana";
console.log(nombreUnd);  // "Ana"
nombreUnd = null;
console.log(nombreUnd);  // null

// undefined — variable declarada pero sin valor
let ciudadUnd: string | undefined;
console.log(ciudadUnd);  // undefined

ciudadUnd = "Madrid";
console.log(ciudadUnd);  // "Madrid"