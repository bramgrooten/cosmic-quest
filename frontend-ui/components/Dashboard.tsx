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
  Stack,
  Text,
  useDisclosure,
} from "@chakra-ui/react";
import Image from "next/image";
import { FaAngleLeft, FaAngleRight, FaPlay } from "react-icons/fa";
import { interpolateHex } from "../helpers/interpolateHex";
import Planet from "../public/planets/planet-2.svg";

export default function Dashboard() {
  const { isOpen, onToggle } = useDisclosure();
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
    <Slide direction="right" in={isOpen} style={{ zIndex: 10 }}>
      <Box
        overflow={"hidden"}
        position={"absolute"}
        right="0"
        w="30%"
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
                    HB23232
                  </Badge>
                </Center>
              </Flex>
            </Stack>
          </Center>
        </Flex>
        <Flex marginTop={10}>
          <Center w="100%">
            <Flex
              bg={interpolateHex("#1B191B", "#000000", 0.3)}
              borderRadius={5}
              paddingX={6}
              paddingY={2}
            >
              Hello
            </Flex>
          </Center>
        </Flex>
      </Box>
    </Slide>
  );
}
