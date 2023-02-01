
import './App.css';
import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [students, setStudents] = useState([]);
  useEffect(() => {
    async function getAllStudents() {
      try {
        const students = await axios.get("http://127.0.0.1:8000/api/student/");
        console.log("student data is: " + students.data);
        setStudents(students.data);
      } catch (error) {
        console.log("errors occurs: " + error);
      }
    }
    getAllStudents();
  }, [])

  return (
    <div className="App">
      <h1>react connection in django</h1>

      {
        students.map((students, index) => {
          return(<>
            <h3 key={index}>Student ID: {students.id}</h3>
            <h3 key={index}>Student Name: {students.studName}</h3>
            <h3 key={index}>Student Email: {students.studEmail}</h3>
            </>
            )
        })
      }
    </div>
  );
}

export default App;
