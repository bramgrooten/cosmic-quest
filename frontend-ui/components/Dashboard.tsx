import { Box, Center, Flex, SimpleGrid, Text } from "@chakra-ui/react";
import Image from "next/image";

export default function Dashboard() {
  return (
    <SimpleGrid columns={1} marginTop={10}>
      <Flex>
        <Center w="100%">
          <Text color={"white"} as="b" height="80px">
            Planet HB1232
          </Text>
        </Center>
      </Flex>
      <Flex>
        <Center w="100%">
          <Image src="/planets/planet.png" alt="me" width="128" height="128" />
        </Center>
      </Flex>
    </SimpleGrid>
  );
}
