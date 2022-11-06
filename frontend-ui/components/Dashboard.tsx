import {
  Badge,
  Box,
  Center,
  Flex,
  Icon,
  IconButton,
  Input,
  InputGroup,
  InputLeftAddon,
  SimpleGrid,
  Slide,
  Spacer,
  Stack,
  Text,
  useDisclosure,
} from "@chakra-ui/react";
import Image from "next/image";
import { useEffect, useState } from "react";
import { FaAngleLeft, FaAngleRight, FaPlay } from "react-icons/fa";
import { interpolateHex } from "../helpers/interpolateHex";
import { Planet } from "./Map";

interface DashboardProps {
  selectedPlanet: Planet | undefined;
}

export default function Dashboard({ selectedPlanet }: DashboardProps) {
  const { isOpen, onToggle } = useDisclosure();

  if (!selectedPlanet) {
    return <></>;
  }
  if (!isOpen) {
    return (
      <IconButton
        position={"absolute"}
        right={"0"}
        aria-label={"Play"}
        margin={3}
        icon={<FaAngleLeft />}
        onClick={onToggle}
      />
    );
  }
  return (
    <Slide direction="right" in={isOpen} style={{ zIndex: 10, width: "30%" }}>
      <Box
        overflow={"hidden"}
        position={"absolute"}
        right="0"
        w="100%"
        h="calc(100vh)"
        bg={interpolateHex("#1B191B", "#000000", 0.05)}
        borderLeft={`0.01rem solid rgba(201, 175, 128, .2)`}
      >
        {/* <Flex>
        <Center w="100%">
          <Text color={"white"} as="b" height="80px">
            Planet HB1232
          </Text>
        </Center>
      </Flex> */}
        <Flex>
          <IconButton
            aria-label={"Play"}
            margin={3}
            icon={<FaAngleRight />}
            onClick={onToggle}
          />
        </Flex>
        <Flex marginTop={10}>
          <Center w="100%">
            <Stack>
              <Flex
                //bg={interpolateHex("#1B191B", "#000000", 0.25)}
                padding={4}
                borderRadius={10}
              >
                <Image
                  src="/planets/planet-2.svg"
                  alt="me"
                  width="128"
                  height="128"
                  color="red"
                />
              </Flex>
              <Flex>
                <Center w="100%">
                  <Badge variant="outline" colorScheme="green">
                    {`${(Math.random() + 1)
                      .toString(36)
                      .substring(2)
                      .toUpperCase()}`}
                  </Badge>
                </Center>
              </Flex>
            </Stack>
          </Center>
        </Flex>
        <Flex marginTop={10}>
          <Center w="100%">
            <Stack gap={5}>
              <Flex
                bg={interpolateHex("#1B191B", "#000000", 0.3)}
                borderRadius={5}
                paddingX={6}
                paddingY={2}
              >
                <Center w="100%">
                  <Text color={"white"}>Radius</Text>
                </Center>
              </Flex>
              <Center w="100%">
                <Text color={"white"}>{selectedPlanet.radius}</Text>
              </Center>
              <Flex
                bg={interpolateHex("#1B191B", "#000000", 0.3)}
                borderRadius={5}
                paddingX={6}
                paddingY={2}
              >
                <Center w="100%">
                  <Text color={"white"}>Mass</Text>
                </Center>
              </Flex>
              <Center w="100%">
                <Text color={"white"}>{selectedPlanet.mass}</Text>
              </Center>
              <Flex
                bg={interpolateHex("#1B191B", "#000000", 0.3)}
                borderRadius={5}
                paddingX={6}
                paddingY={2}
              >
                <Text color={"white"}>Temperature</Text>
              </Flex>
              <Center w="100%">
                <Text color={"white"}>{selectedPlanet.temperature}</Text>
              </Center>
            </Stack>
          </Center>
        </Flex>
      </Box>
    </Slide>
  );
}
