import { useEffect, useState } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";
import PostData from "./PostData";

function GetData() {
  const [students, setStudents] = useState([]);
  const [editStudent, setEditStudent] = useState({});
  const [showEditForm, setShowEditForm] = useState(false);

  const handleEdit = (student) => {
    console.log("data is: " + student.id);
    setEditStudent(student);
    setShowEditForm(true);
  };

  const handleUpdate = (student) => {
    const url_update = `http://127.0.0.1:8000/api/api/update/${student.id}`;
    try {
      console.log("update calling ..." + student.id);
      axios.put(url_update, student).then(() => {
        setStudents((prevState) => {
          // Replace the updated student in the students list
          const newStudents = prevState.map((item) => {
            if (item.id === student.id) {
              return student;
            }
            return item;
          });
          return newStudents;
        });
        setShowEditForm(false);
      });
    } catch (error) {
      console.log("errors occurs: " + error);
    }
  };
  useEffect(() => {
    async function getAllStudents() {
      try {
        const students = await axios.get(
          "http://127.0.0.1:8000/api/api/students"
        );
        // console.log("student data is: " + students.data);
        setStudents(students.data);
      } catch (error) {
        console.log("errors occurs: " + error);
      }
    }
    getAllStudents();
  }, []);

  const handleDelete = (idDelete) => {
    const url_delete = `http://127.0.0.1:8000/api/api/delete/${idDelete}`;
    console.log("delete call..." + idDelete);
    try {
      axios.delete(url_delete).then(() => {
        setStudents((prevState) => {
          const newStudents = prevState.filter(
            (student) => student.id !== idDelete
          );
          return newStudents;
        });
      });
    } catch (error) {
      console.log("errors occurs: " + error);
    }
  };

  return (
    <>
      {showEditForm ? (
        <div className="container col-sm-6 m-5">
          <form
            onSubmit={(event) => {
              event.preventDefault();
              handleUpdate(editStudent);
            }}
          >
            <div className="form-group">
              <input
                type="text"
                className="form-control m-1"
                name="studentName"
                value={editStudent.studentName}
                onChange={(event) => {
                  setEditStudent({
                    ...editStudent,
                    studentName: event.target.value,
                  });
                }}
              />
            </div>
            <div className="form-group">
              <input
                type="email"
                className="form-control m-1"
                name="studentEmail"
                value={editStudent.studentEmail}
                onChange={(event) => {
                  setEditStudent({
                    ...editStudent,
                    studentEmail: event.target.value,
                  });
                }}
              />
            </div>
            <button type="submit" className="btn btn-primary m-2">
              Update
            </button>
            <button
              type="button"
              className="btn btn-secondary m-2"
              onClick={() => setShowEditForm(false)}
            >
              Cancel
            </button>
          </form>
        </div>
      ) : (
        <PostData />
      )}
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
                  <td>{students.studentName}</td>
                  <td>{students.studentEmail}</td>
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
                  <td>
                    <Button
                      variant="outline-success"
                      value="Edit"
                      onClick={() => {
                        handleEdit(students);
                      }}
                    >
                      Edit
                    </Button>
                  </td>
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
