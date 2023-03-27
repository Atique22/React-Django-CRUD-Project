import "./App.css";
import GetData from "./components/GetData";
import VideoCapture from "./components/VideoCaptureFrame";
import ViewVideoFrameData from "./components/ViewVideoFrameData";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Link to="/">
          <Button variant="success" className=" m-2">
            CRUD-with User Data
          </Button>
        </Link>
        <Link to="/video">
          <Button variant="success" className=" m-2">
            CRUD-with Video Frames
          </Button>
        </Link>
        <Link to="/ViewVideoFrameData">
          <Button variant="success" className=" m-2">
            View Video Frames
          </Button>
        </Link>

        <Routes>
          <Route exact path="/" element={<GetData />} />
          <Route exact path="/video" element={<VideoCapture />} />
          <Route
            exact
            path="/ViewVideoFrameData"
            element={<ViewVideoFrameData />}
          />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
