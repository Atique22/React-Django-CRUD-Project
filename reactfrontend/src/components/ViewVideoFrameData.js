import { useEffect, useState } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
// import Button from "react-bootstrap/Button";

function GetData() {
  const [frameData, setFrameData] = useState([]);
  useEffect(() => {
    async function getAllFrameData() {
      try {
        const frameData = await axios.get(
          "http://127.0.0.1:8000/api/api/frameDataStorage"
        );
        // console.log("myFrame data is: " + frameData.data);
        setFrameData(frameData.data);
      } catch (error) {
        console.log("errors occurs: " + error);
      }
    }
    getAllFrameData();
  }, []);

  return (
    <>
      <div className="container col-sm-6 m-5">
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>FRAME</th>
              <th> Name</th>
              <th> Comment</th>
              <th> Status</th>
            </tr>
          </thead>
          <tbody>
            {frameData.map((frameData, index) => {
              return (
                <tr key={index}>
                  <td className="w-25">
                    <img
                      src={frameData.frame_image}
                      className="img-fluid img-thumbnail"
                      alt={frameData.frame_image}
                    />
                  </td>
                  <td className=" text-truncate">{frameData.frame_name}</td>
                  <td className=" text-truncate">{frameData.frame_comment}</td>
                  <td className=" text-truncate">{frameData.frame_type}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      </div>
    </>
  );
}

export default GetData;
