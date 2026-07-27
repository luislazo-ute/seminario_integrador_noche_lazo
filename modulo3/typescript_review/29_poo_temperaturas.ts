class Temperatura {
  valorCelsius: number;
  valorFarenheit: number;

  constructor(celsius: number, farenheit: number) {
    this.valorCelsius = celsius;
    this.valorFarenheit = farenheit;
  }

  aFahrenheit(): number {
    return this.valorCelsius * 9 / 5 + 32;
  }

  aKelvin(): number {
    return this.valorCelsius + 273.15;
  }
  
  aCelsius(): number {
    return (this.valorFarenheit - 32) * 5 / 9;
  }

  describir(): string {
    return (
      `${this.valorCelsius}°C = ` +
      `${this.aFahrenheit()}°F = ` +
      `${this.aKelvin()}K`
    );

  }

  describirFarenheit(): string {
    return (
      `${this.valorFarenheit}°F = ` +
      `${this.aCelsius()}°C = `
    );  
  }
}

const hervor = new Temperatura(100, 212);
const congelacion = new Temperatura(0, 32);

console.log(hervor.describir());
console.log(hervor.describirFarenheit());// 100°C = 212°F = 373.15K
console.log(congelacion.describir()); // 0°C = 32°F = 273.15K
console.log(congelacion.describirFarenheit()); // 32°F = 0°C = 273.15K