import React, { useRef } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
function PostData() {
  const formRef = useRef(null);
  async function sendData() {
    const formData = new FormData(formRef.current);
    console.log(formData);
    if (!formData) {
      console.log("Please enter student name and age");
      return;
    }
    try {
      console.log(formData);
      const response = await axios
        .post("http://127.0.0.1:8000/api/api/students", formData)
        .then();
      console.log("data send" + response.data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="container col-sm-6 m-5">
      <Form ref={formRef}>
        <Form.Group className="mb-3" controlId="formBasicName">
          <Form.Control
            name="studentName"
            type="text"
            placeholder="Enter name"
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Control
            name="studentEmail"
            type="email"
            placeholder="Enter email"
          />
        </Form.Group>

        <Button
          variant="primary"
          type="submit"
          onClick={() => {
            sendData();
          }}
        >
          Submit
        </Button>
      </Form>
    </div>
  );
}
export default PostData;
