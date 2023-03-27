import React, { useRef } from "react";
import axios from "axios";
import myVideo from "../assets/video.mp4";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

function VideoCapture() {
  const navigate = useNavigate();
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const formFrameRef = useRef(null);
  let dataURL;
  const captureFrame = async () => {
    console.log("capture get");
    const canvas = canvasRef.current;
    const video = videoRef.current;
    dataURL = canvas.toDataURL("image/jpeg");
    console.log("capture at front page access:" + dataURL);
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
    dataURL = canvas.toDataURL("image/jpeg");
  };
  async function sendFrameData() {
    const formFrameData = new FormData(formFrameRef.current);
    console.log(formFrameRef);
    if (!formFrameData) {
      console.log("Please enter valid data");
      return;
    } else if (!dataURL) {
      console.log(" image url is not access:" + dataURL);
    }
    try {
      const formData = new FormData();
      console.log("date url is:" + dataURL);
      formData.append("frameName", formFrameData.get("frameName"));
      formData.append("frameType", formFrameData.get("frameType"));
      formData.append("frameComment", formFrameData.get("frameComment"));
      formData.append("frameImage", dataURL);

      await axios
        .post("http://127.0.0.1:8000/api/api/frameDataStorage", formData)
        .then()
        .then((data) => {
          console.log("send data: " + data);
          alert("Frame data created successfully!");
          navigate("/ViewVideoFrameData");
        });
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <div className="display-block">
        <video controls ref={videoRef}>
          <source src={myVideo} type="video/mp4" />
        </video>
        <div>
          <Button onClick={captureFrame} variant="success">
            Capture Frame
          </Button>
        </div>
      </div>

      <div className="card m-5">
        <canvas ref={canvasRef} />
        <form
          className="m-2"
          ref={formFrameRef}
          onSubmit={(event) => {
            event.preventDefault();
            sendFrameData();
          }}
        >
          <div className="card-body">
            <h5 className="card-title">Frame Set Details</h5>

            <div className="form-group">
              <input
                type="text"
                name="frameName"
                className="form-control m-2"
                placeholder="Enter Name"
              />
            </div>
            <div className="form-group">
              <select
                className="form-control m-2"
                name="frameType"
                id="selectId"
              >
                <option>Select Your Choice- Middle/Edge/Missed Ball </option>
                <option>Middle Ball </option>
                <option>Edge Ball </option>
                <option>Missed Ball </option>
              </select>
            </div>
            <div className="form-group">
              <textarea
                name="frameComment"
                className="form-control m-2"
                id="exampleFormControlTextarea1"
                rows="3"
                placeholder="Comment here!"
              ></textarea>
            </div>
          </div>
          <Button variant="primary" type="submit">
            Save
          </Button>
        </form>
      </div>
    </div>
  );
}
export default VideoCapture;
