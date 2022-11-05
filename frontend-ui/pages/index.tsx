import { AddIcon, MinusIcon } from "@chakra-ui/icons";
import { Box, Grid, GridItem, SimpleGrid } from "@chakra-ui/layout";
import { ButtonGroup, Flex, IconButton, Spacer } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import Dashboard from "../components/Dashboard";
import Map, { Planet, PlanetState, Star } from "../components/Map";
import useWindowDimensions from "../hooks/useWindowDimensions";

export type GalaxyData = {
  star_list: Star[];
  planet_list: Planet[];
  human_colony: number[];
  connections: [number, number][];
  new_connections: [number, number][];
  scores: number[];
};

export default function Page() {
  const { height, width } = useWindowDimensions();
  const [scale, setScale] = useState(1);
  const [bodies, setBodies] = useState<GalaxyData>();

  useEffect(() => {
    fetch("http://127.0.0.1:5000/move")
      .then((res) => res.json())
      .then((data: GalaxyData) => {
        console.log(data);
        setBodies(data);
      });
  }, []);

  return (
    <Grid h="calc(100vh)" templateColumns="repeat(3, 1fr)" bg="#1B191B">
      <GridItem colSpan={2}>
        <Flex margin={3} position={"absolute"}>
          <ButtonGroup gap="1">
            <IconButton
              aria-label={"Zoom in"}
              icon={<AddIcon />}
              onClick={() => setScale((prev) => prev + 1)}
            />
            <IconButton
              aria-label={"Zoom out"}
              icon={<MinusIcon />}
              onClick={() => setScale((prev) => prev - 1)}
            />
          </ButtonGroup>
        </Flex>
        {bodies && (
          <Map
            width={(width * 2) / 3}
            height={height}
            bodies={bodies}
            scale={scale}
          />
        )}
      </GridItem>
      <GridItem>
        <Dashboard />
      </GridItem>
    </Grid>
  );
}
