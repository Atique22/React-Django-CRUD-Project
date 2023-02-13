import React, { useRef, useEffect } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
// import { Navigate} from "react-router-dom";
function PostData() {
  const formRef = useRef(null);
  // const [studEmail, setStudEmail] = useState('');
  // const id = null;
  const sendData = async (event) => {
    const formData = new FormData(formRef.current);
    console.log(formData);
    if (!formData) {
      console.log("Please enter student name and age");
      return;
    }
    try {
      console.log(formData);
      const response = await axios.post(
        "http://127.0.0.1:8000/api/student/",
        formData
      );
      console.log("data send" + response.data);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    console.log("USE EFFECT CALL");
  });

  return (
    <div className="container col-sm-6 m-5">
      <Form ref={formRef}>
        <Form.Group className="mb-3" controlId="formBasicName">
          <Form.Control name="studName" type="text" placeholder="Enter name" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Control
            name="studEmail"
            type="email"
            placeholder="Enter email"
          />
        </Form.Group>

        <Button variant="primary" type="submit" onClick={(e) => sendData(e)}>
          Submit
        </Button>
      </Form>
    </div>
  );
}
export default PostData;
