import { useEffect, useState } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";
function GetData() {
  const [students, setStudents] = useState([]);
  useEffect(() => {
    async function getAllStudents() {
      try {
        const students = await axios.get("http://127.0.0.1:8000/api/student/");
        // console.log("student data is: " + students.data);
        setStudents(students.data);
      } catch (error) {
        console.log("errors occurs: " + error);
      }
    }
    getAllStudents();
  }, []);

  const handleDelete = (idDelete) => {
    const url_delete = `http://127.0.0.1:8000/api/delete/${idDelete}/`;
    console.log("delete call..." + idDelete);
    try {
      axios.get(url_delete);
    } catch (error) {
      console.log("errors occurs: " + error);
    }
  };
  return (
    <div className="container col-sm-6 m-5">
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th> Name</th>
            <th> Email</th>
          </tr>
        </thead>
        <tbody>
          {students.map((students, index) => {
            return (
              <tr key={index}>
                <td> {students.id}</td>
                <td>{students.studName}</td>
                <td>{students.studEmail}</td>
                <td>
                  <Button
                    variant="outline-danger"
                    value="Delete"
                    onClick={() => {
                      handleDelete(students.id);
                    }}
                  >
                    Delete
                  </Button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </Table>
    </div>
  );
}

export default GetData;
