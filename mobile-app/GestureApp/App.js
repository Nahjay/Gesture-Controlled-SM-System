import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import React from 'react';

export default function App() {

  // Function to start Gesture Recognition
  function startGestureRecognition() {
    console.log("Starting Gesture Recognition...")

    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const handleClick = async () => {
      try {
        const response = await fetch('http://192.168.0.105:5000/start_gesture_recognition');
        const data = await response.json();
        setData(data);
      }
      catch (error) {
        setError(error);
      }
    };


    return (
      <View style={styles.container}>
        <Text>Gesture Recognition Project!</Text>

        {/* Add a button to initiate Gesture Recognition */}
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
}
