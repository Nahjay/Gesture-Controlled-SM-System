import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import React from 'react';

export default function App() {
  const [data, setData] = React.useState(null);
  const [error, setError] = React.useState(null);

  // Function to start Gesture Recognition
  const startGestureRecognition = async () => {
    console.log("Starting Gesture Recognition...");

    try {
      const response = await fetch('http://192.168.0.161:8080/start_gesture_recognition');
      const data = await response.json();
      setData(data);
    } catch (error) {
      setError(error);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Gesture Recognition Project!</Text>
      <Button title='Start Gesture Recognition' onPress={startGestureRecognition} />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});