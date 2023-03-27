import "./App.css";
import GetData from "./components/GetData";
import VideoCapture from "./components/VideoCaptureFrame";
import "bootstrap/dist/css/bootstrap.min.css";
function App() {
  return (
    <div className="App">
      <GetData />
      <VideoCapture />
    </div>
  );
}

export default App;
