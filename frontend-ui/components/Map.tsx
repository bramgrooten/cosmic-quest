import dynamic from "next/dynamic";
import p5Types from "p5";

// Will only import `react-p5` on client-side
const Sketch = dynamic(() => import("react-p5").then((mod) => mod.default), {
  ssr: false,
});

export enum PlanetState {
  DISCOVERED = "#C9AF80",
  SCANNED = "#000",
}

export type Star = {
  x: number;
  y: number;
  planet_list: Planet[];
};

type Planet = {
  x: number;
  y: number;
  dist_to_star: number;
  mass: number;
  radius: number;
  orbital_period: number;
  star_mass: number;
  star_radius: number;
  star_temperature: number;
  star_age: number;
  status: PlanetState;
};

interface MapProps {
  width: number;
  height: number;
  scale: number;
  bodies: Star[];
}

function scaleCoordinate(
  x: number,
  y: number,
  screenWidth: number,
  screenHeight: number
) {
  const factorY = 100000 / screenHeight;
  const factorX = 100000 / screenWidth;
  const scaledX = x / factorX + (1 / 2) * screenWidth;
  const scaledY = y / factorY + (1 / 2) * screenHeight;
  return { scaledX, scaledY };
}

export default function Map({ width, height, bodies, scale }: MapProps) {
  // See annotations in JS for more information
  const setup = (p5: p5Types, canvasParentRef: Element) => {
    const cnv = p5.createCanvas(width, height).parent(canvasParentRef);
    //cnv.mouseWheel((event: any) => zoomMap(p5, event));
  };

  const draw = (p5: p5Types) => {
    p5.background("#1B191B");

    bodies.forEach((star) => {
      drawStar(p5, star);
      star.planet_list.forEach((planet) => {
        drawPlanet(p5, planet);
      });
    });

    //drawStar(p5, { x: 600, y: 600, status: PlanetState.DISCOVERED });
  };

  /*
  const zoomMap = (p5: p5Types, event: any) => {
    zoom += 0.005 * event.delta;
    zoom = p5.constrain(zoom, 0.05, 10);
    //uncomment to block page scrolling
    return false;
  };
  */

  const drawPlanet = (p5: p5Types, planet: Planet) => {
    let color = p5.color(planet.status);
    p5.fill(color);
    p5.noStroke();

    const { scaledX, scaledY } = scaleCoordinate(
      planet.x,
      planet.y,
      width,
      height
    );

    p5.circle(scaledX, scaledY, scale);
  };

  const drawStar = (p5: p5Types, star: Star) => {
    let color = p5.color("#C9AF80");
    p5.fill(color);
    p5.noStroke();
    let angle = p5.TWO_PI / 4;
    let halfAngle = angle / 2.0;
    const radius1 = scale;
    const radius2 = radius1 * 4;
    p5.beginShape();
    for (let a = 0; a < p5.TWO_PI; a += angle) {
      let sx = star.x + p5.cos(a) * radius2;
      let sy = star.y + p5.sin(a) * radius2;
      p5.vertex(sx, sy);
      sx = star.x + p5.cos(a + halfAngle) * radius1;
      sy = star.y + p5.sin(a + halfAngle) * radius1;
      p5.vertex(sx, sy);
    }
    p5.endShape("close");
  };

  return <Sketch setup={setup} draw={draw} />;
}
