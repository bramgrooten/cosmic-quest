import { Center, Grid, GridItem } from "@chakra-ui/layout";
import { ButtonGroup, Flex, IconButton } from "@chakra-ui/react";
import { useState } from "react";
import Dashboard from "../components/Dashboard";
import Map, { Planet, Star } from "../components/Map";
import useWindowDimensions from "../hooks/useWindowDimensions";
import { FaPlay, FaPause, FaRedo } from "react-icons/fa";

export type GalaxyData = {
  star_list: Star[];
  planet_list: Planet[];
  human_colony: number[];
  connections: [number, number][];
  new_human_colony_planets: number[];
  new_connections: [number, number][];
  scores: number[];
};

export default function Page() {
  const { height, width } = useWindowDimensions();
  const [scale, setScale] = useState(1);
  const [bodies, setBodies] = useState<GalaxyData>();
  const [refresh, setRefresh] = useState<ReturnType<typeof setTimeout>>();
  const [selectedPlanet, setSelectedPlanet] = useState<Planet>();

  const fetchGalaxy = () => {
    fetch("http://127.0.0.1:5000/move")
      .then((res) => res.json())
      .then((data: GalaxyData) => {
        setBodies(data);
      });
  };

  const resetGalaxy = () => {
    fetch("http://127.0.0.1:5000/reset")
      .then((res) => res.json())
      .then((data: GalaxyData) => {
        setBodies(data);
      });
  };

  const setSimulationRefresh = () => {
    if (refresh) {
      clearInterval(refresh);
    }

    const interval = setInterval(() => {
      fetchGalaxy();
    }, 2000);
    setRefresh(interval);
  };

  return (
    <Grid h="calc(100vh)" templateColumns="repeat(3, 1fr)" bg="#1B191B">
      <GridItem colSpan={3}>
        <Flex marginTop={3} w="100%" position={"absolute"}>
          <Center w="100%">
            <ButtonGroup gap="1">
              {refresh ? (
                <IconButton
                  aria-label={"Pause"}
                  icon={<FaPause />}
                  onClick={() => {
                    clearInterval(refresh);
                    setRefresh(undefined);
                  }}
                />
              ) : (
                <IconButton
                  aria-label={"Play"}
                  icon={<FaPlay />}
                  onClick={() => setSimulationRefresh()}
                />
              )}
              <IconButton
                aria-label={"Reset"}
                icon={<FaRedo />}
                onClick={() => resetGalaxy()}
              />
            </ButtonGroup>
          </Center>
        </Flex>
        <Dashboard selectedPlanet={selectedPlanet} />

        {bodies && (
          <Map
            width={width}
            height={height}
            bodies={bodies}
            scale={scale}
            setSelectedPlanet={setSelectedPlanet}
          />
        )}
      </GridItem>
    </Grid>
  );
}
