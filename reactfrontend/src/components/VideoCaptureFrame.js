import React, { useRef } from "react";
import axios from "axios";
import myVideo from "../assets/video.mp4";
import Button from "react-bootstrap/Button";

function VideoCapture() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const captureFrame = async () => {
    const canvas = canvasRef.current;
    const video = videoRef.current;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL("image/jpeg");

    try {
      const response = await axios.post("/api/capture-frame", { dataURL });
      console.log("Frame captured and saved:", response.data);
    } catch (err) {
      console.error("Error capturing and saving frame:", err);
    }
  };

  return (
    <div>
      <video controls ref={videoRef}>
        <source src={myVideo} type="video/mp4" />
      </video>
      <canvas ref={canvasRef} style={{ display: "block" }} />
      <Button onClick={captureFrame}>Capture Frame</Button>
    </div>
  );
}
export default VideoCapture;
