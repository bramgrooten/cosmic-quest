import { AddIcon, MinusIcon } from "@chakra-ui/icons";
import { Box, Grid, GridItem, SimpleGrid } from "@chakra-ui/layout";
import { ButtonGroup, Flex, IconButton, Spacer } from "@chakra-ui/react";
import { useState } from "react";
import Dashboard from "../components/Dashboard";
import Map, { PlanetState, Star } from "../components/Map";
import useWindowDimensions from "../hooks/useWindowDimensions";

const bodies: Star[] = [
  {
    x: -31697.85283724629,
    y: -13112.26219919985,
    planet_list: [
      {
        x: -31872.136920951052,
        y: -12912.964456833628,
        dist_to_star: 264.7537194168984,
        mass: 2648.9233588221114,
        radius: 8.770454023451988,
        orbital_period: 27271.459691319356,
        star_mass: 71.91268873661137,
        star_radius: 69.68870230335833,
        star_temperature: 22594.1430455158,
        star_age: 6.139728594264926,
        status: PlanetState.DISCOVERED,
      },
      {
        x: -31994.550549271706,
        y: -13219.419987177569,
        dist_to_star: 315.455739915118,
        mass: 689.4187765331259,
        radius: 0.506533241651842,
        orbital_period: 20239.508372942426,
        star_mass: 52.036972878757524,
        star_radius: 14.013432655566668,
        star_temperature: 24158.032986263373,
        star_age: 10.311535174646474,
        status: PlanetState.DISCOVERED,
      },
      {
        x: -31948.54427050122,
        y: -13094.658746185583,
        dist_to_star: 251.30872699816368,
        mass: 970.6774240282624,
        radius: 3.4709883690945738,
        orbital_period: 48926.87850523201,
        star_mass: 26.81034770757625,
        star_radius: 18.440547533510145,
        star_temperature: 24779.6437908377,
        star_age: 0.28637583165763597,
        status: PlanetState.DISCOVERED,
      },
    ],
  },
  {
    x: 33050.234877084295,
    y: 17124.139088987857,
    planet_list: [
      {
        x: 32930.23369662552,
        y: 17031.892237164484,
        dist_to_star: 151.3597204768303,
        mass: 3274.4346980623304,
        radius: 14.807686867759612,
        orbital_period: 50007.872051401755,
        star_mass: 30.394481190565784,
        star_radius: 6.6875863664881345,
        star_temperature: 6142.039595542248,
        star_age: 5.2956008102032515,
        status: PlanetState.DISCOVERED,
      },
      {
        x: 33260.643728395575,
        y: 17165.841039238167,
        dist_to_star: 214.5016022429972,
        mass: 2474.205868409796,
        radius: 3.5346041603940437,
        orbital_period: 53206.317785489424,
        star_mass: 77.07057350373036,
        star_radius: 11.352802471271229,
        star_temperature: 17635.088137204508,
        star_age: 1.768117419556373,
        status: PlanetState.DISCOVERED,
      },
      {
        x: 32880.62933152674,
        y: 17328.15438258443,
        dist_to_star: 265.3078986859809,
        mass: 1138.3291046514898,
        radius: 12.807942971025174,
        orbital_period: 57930.90020771254,
        star_mass: 70.77177406770232,
        star_radius: 63.01723395191756,
        star_temperature: 22651.484544933483,
        star_age: 8.889700802567393,
        status: PlanetState.DISCOVERED,
      },
    ],
  },
];

export default function Page() {
  const { height, width } = useWindowDimensions();
  const [scale, setScale] = useState(1);

  return (
    <Grid h="calc(100vh)" templateColumns="repeat(3, 1fr)" bg="#1B191B">
      <GridItem colSpan={2}>
        <Flex marginTop={3}>
          <Spacer />
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

        <Map
          width={(width * 2) / 3}
          height={height}
          bodies={bodies}
          scale={scale}
        />
      </GridItem>
      <GridItem>
        <Dashboard />
      </GridItem>
    </Grid>
  );
}