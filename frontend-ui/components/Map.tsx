import { popper } from "@popperjs/core";
import dynamic from "next/dynamic";
import { release } from "os";
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
  temperature: number;
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

function scaleWithZoom(scale: number, currentScale: number) {
  return scale * (2 / currentScale) - 0.2;
}

export default function Map({ width, height, bodies, scale }: MapProps) {
  const zoomSensitivity = 0.1;
  // Scale while drawing objects
  // Start with a scale of 1
  let currentScale = 1;
  // Transformation while drawing objects
  // Start with no transformation
  let transformX = 0;
  let transformY = 0;
  let isMouseDragged = false;
  let mousePressedX: number | null = null;
  let mousePressedY: number | null = null;
  // See annotations in JS for more information
  const setup = (p5: p5Types, canvasParentRef: Element) => {
    const cnv = p5.createCanvas(width, height).parent(canvasParentRef);
    cnv.mouseWheel((event: any) => mouse(p5, event));
    cnv.mousePressed(() => press(p5));
    cnv.mouseReleased(() => release());
    cnv.mouseMoved(() => drag(p5));
  };

  const draw = (p5: p5Types) => {
    p5.background("#1B191B");
    p5.push();
    p5.translate(transformX, transformY);
    p5.scale(currentScale);
    bodies.forEach((star) => {
      drawStar(p5, star);
      star.planet_list.forEach((planet) => {
        drawPlanet(p5, planet);
      });
    });
    p5.pop();
  };

  const release = () => {
    mousePressedX = null;
    mousePressedY = null;
    isMouseDragged = false;
  };

  const press = (p5: p5Types) => {
    mousePressedX = p5.mouseX;
    mousePressedY = p5.mouseY;
    isMouseDragged = true;
  };

  const mouse = (p5: p5Types, event: any) => {
    event.preventDefault();
    // Determine the scale factor based on zoom sensitivity
    let scaleFactor = null;
    if (event.deltaY < 0) {
      // Zoom in
      scaleFactor = 1 + zoomSensitivity;
    } else {
      // Zoom out
      scaleFactor = 1 - zoomSensitivity;
    }

    // Apply transformation and scale incrementally
    currentScale = currentScale * scaleFactor;
    transformX = p5.mouseX - p5.mouseX * scaleFactor + transformX * scaleFactor;
    transformY = p5.mouseY - p5.mouseY * scaleFactor + transformY * scaleFactor;

    // Disable page scroll
    return false;
  };

  const drag = (p5: any) => {
    if (isMouseDragged) {
      transformX += -(p5.mouseX - mousePressedX!) * 0.3;
      transformY += -(p5.mouseY - mousePressedY!) * 0.3;
    }
  };

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

    p5.circle(scaledX, scaledY, scaleWithZoom(scale, currentScale));
  };

  const drawStar = (p5: p5Types, star: Star) => {
    const { scaledX, scaledY } = scaleCoordinate(star.x, star.y, width, height);

    let color = p5.color("#C9AF80");
    p5.fill(color);
    p5.noStroke();
    let angle = p5.TWO_PI / 4;
    let halfAngle = angle / 2.0;
    const radius1 = scaleWithZoom(scale, currentScale);
    const radius2 = radius1 * 4;
    p5.beginShape();
    for (let a = 0; a < p5.TWO_PI; a += angle) {
      let sx = scaledX + p5.cos(a) * radius2;
      let sy = scaledY + p5.sin(a) * radius2;
      p5.vertex(sx, sy);
      sx = scaledX + p5.cos(a + halfAngle) * radius1;
      sy = scaledY + p5.sin(a + halfAngle) * radius1;
      p5.vertex(sx, sy);
    }
    p5.endShape("close");
  };

  return <Sketch setup={setup} draw={draw} />;
}
