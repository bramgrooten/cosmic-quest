import dynamic from "next/dynamic";
import p5Types from "p5";
import { useRef } from "react";
import { interpolateHex } from "../helpers/interpolateHex";
import { GalaxyData } from "../pages";

export enum PlanetState {
  DISCOVERED = "#C9AF80",
  SCANNED = "#000",
}

export type Star = {
  x: number;
  y: number;
  planet_list: Planet[];
};

export type Planet = {
  x: number;
  y: number;
  dist_to_star: number;
  mass: number;
  radius: number;
  temperature: number;
  status: PlanetState;
  habitable: number;
};

interface MapProps {
  width: number;
  height: number;
  scale: number;
  bodies: GalaxyData;
  setSelectedPlanet: any;
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
  return scale * (0.8 / (currentScale - 0.2) + 0.2);
}

export default function Map({
  width,
  height,
  bodies,
  scale,
  setSelectedPlanet,
}: MapProps) {
  // Will only import `react-p5` on client-side
  const Sketch = dynamic(() => import("react-p5").then((mod) => mod.default), {
    ssr: false,
  });
  const zoomSensitivity = 0.1;
  // Scale while drawing objects
  // Start with a scale of 1
  let currentScale = useRef(1);
  // Transformation while drawing objects
  // Start with no transformation
  let transformX = useRef(0);
  let transformY = useRef(0);
  let isMouseDragged = false;
  let mousePressedX = useRef(0);
  let mousePressedY = useRef(0);
  let mouseX = useRef(1000);
  let mouseY = useRef(1000);
  let curPlanet = useRef<Planet | undefined>();
  // See annotations in JS for more information
  const setup = (p5: p5Types, canvasParentRef: Element) => {
    const cnv = p5.createCanvas(width, height).parent(canvasParentRef);
    cnv.mouseWheel((event: any) => mouse(p5, event));
    cnv.mousePressed(() => press(p5));
    cnv.mouseReleased(() => release());
    cnv.mouseMoved(() => drag(p5));
    cnv.mouseClicked(() => click(p5));
  };

  const draw = (p5: p5Types) => {
    p5.background("#1B191B");
    p5.push();
    p5.translate(transformX.current, transformY.current);
    p5.scale(currentScale.current);
    let planetIndex = 0;
    bodies.star_list.forEach((star) => {
      drawStar(p5, star);
      star.planet_list.forEach((planet) => {
        planet["habitable"] = bodies.scores[planetIndex];
        if (currentScale.current > 6) {
          drawPlanet(p5, planet);
        }
        planetIndex++;
      });
    });
    drawColonies(p5, bodies.human_colony, bodies.connections, "#0000FF");
    drawColonies(
      p5,
      bodies.new_human_colony_planets,
      bodies.new_connections,
      "#A020F0"
    );
    if (curPlanet.current) {
      drawBox(p5, curPlanet.current);
    }

    p5.pop();
  };

  const click = (p5: p5Types) => {
    const x =
      p5.mouseX / currentScale.current -
      transformX.current / currentScale.current;
    const y =
      p5.mouseY / currentScale.current -
      transformY.current / currentScale.current;

    let dist = -1;
    let closestPlanet = bodies.planet_list[0];

    bodies.planet_list.forEach((planet) => {
      const { scaledX, scaledY } = scaleCoordinate(
        planet.x,
        planet.y,
        width,
        height
      );
      const a = scaledX - x;
      const b = scaledY - y;
      const c = Math.hypot(a, b);

      if (c < dist) {
        dist = c;
        closestPlanet = planet;
      }

      if (dist === -1) {
        dist = c;
        closestPlanet = planet;
      }
    });

    setSelectedPlanet(closestPlanet);
    curPlanet.current = closestPlanet;
  };

  const release = () => {
    mousePressedX.current = 0;
    mousePressedY.current = 0;
    isMouseDragged = false;
  };

  const press = (p5: p5Types) => {
    mousePressedX.current = p5.mouseX;
    mousePressedY.current = p5.mouseY;
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
    if (p5.mouseX !== 0 && p5.mouseY !== 0) {
      mouseX.current = p5.mouseX;
      mouseY.current = p5.mouseY;
    }

    // Apply transformation and scale incrementally
    if (
      !(currentScale.current * scaleFactor > 40) &&
      !(currentScale.current * scaleFactor < 0.65)
    ) {
      currentScale.current = currentScale.current * scaleFactor;
      transformX.current =
        mouseX.current -
        mouseX.current * scaleFactor +
        transformX.current * scaleFactor;
      transformY.current =
        mouseY.current -
        mouseY.current * scaleFactor +
        transformY.current * scaleFactor;
    }

    // Disable page scroll
    return false;
  };

  const drag = (p5: p5Types) => {
    mouseX.current = p5.mouseX;
    mouseY.current = p5.mouseY;

    if (isMouseDragged) {
      transformX.current += (mouseX.current - mousePressedX.current!) * 0.3;
      transformY.current += (mouseY.current - mousePressedY.current!) * 0.3;
    }
  };

  const drawBox = (p5: p5Types, planet: Planet) => {
    p5.stroke("red");
    p5.noFill();
    const { scaledX, scaledY } = scaleCoordinate(
      planet.x,
      planet.y,
      width,
      height
    );
    const scaledSize = scaleWithZoom(scale * 8, currentScale.current);
    const offset = (1 / 2) * scaledSize;
    p5.square(scaledX - offset, scaledY - offset, scaledSize);
  };

  const drawColonies = (
    p5: p5Types,
    colonies: number[],
    connections: [number, number][],
    color: string
  ) => {
    p5.fill(p5.color(color));
    p5.noStroke();

    colonies.forEach((colony) => {
      const planet = bodies.planet_list[colony];
      const { scaledX, scaledY } = scaleCoordinate(
        planet.x,
        planet.y,
        width,
        height
      );
      p5.circle(
        scaledX,
        scaledY,
        scaleWithZoom(scale * 1.5, currentScale.current) * 3
      );
    });

    p5.stroke(color);
    p5.strokeWeight(scaleWithZoom(scale * 0.7, currentScale.current));
    connections.forEach((connection) => {
      const planetStart = bodies.planet_list[connection[0]];
      const planetEnd = bodies.planet_list[connection[1]];

      const { scaledX: scaledStartX, scaledY: scaledStartY } = scaleCoordinate(
        planetStart.x,
        planetStart.y,
        width,
        height
      );
      const { scaledX: scaledEndX, scaledY: scaledEndY } = scaleCoordinate(
        planetEnd.x,
        planetEnd.y,
        width,
        height
      );
      p5.line(scaledStartX, scaledStartY, scaledEndX, scaledEndY);
    });
  };

  const drawPlanet = (p5: p5Types, planet: Planet) => {
    let color = p5.color(
      interpolateHex("#CD5757", "#00FF00", planet.habitable / 100)
    );
    p5.fill(color);
    p5.noStroke();

    const { scaledX, scaledY } = scaleCoordinate(
      planet.x,
      planet.y,
      width,
      height
    );

    p5.circle(
      scaledX,
      scaledY,
      scaleWithZoom(scale * 1.5, currentScale.current)
    );
  };

  const drawStar = (p5: p5Types, star: Star) => {
    const { scaledX, scaledY } = scaleCoordinate(star.x, star.y, width, height);

    let color = p5.color("#C9AF80");
    p5.fill(color);
    p5.noStroke();
    let angle = p5.TWO_PI / 4;
    let halfAngle = angle / 2.0;
    const radius1 = scaleWithZoom(scale, currentScale.current);
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
