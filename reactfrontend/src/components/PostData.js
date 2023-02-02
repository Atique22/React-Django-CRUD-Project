import React, { useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function PostData() {


    const defaultValue = {
        username: '',
        UserEmail: ''
    }
    const [userData, setUserData] = useState(defaultValue);
    const onValueChange = (e) => {
        // console.log(userData);
        setUserData({...userData, [e.target.name]: e.target.value });
        console.log(userData);
    }

    const sendData = async(e) => {
        e.preventDefault()
        console.log("data send: " + userData)
        try {
            alert("Api calling.url");
            const response = await axios.post('http://127.0.0.1:8000/api/student/', {userData});
            console.log(response.userData);
            console.log("data send: " + userData)
        } catch (error) {
            console.error(error);
        }
    };


    return (
        <div className='container col-sm-6 m-5'>
            <Form>
                <Form.Group className="mb-3" controlId="formBasicName">
                    <Form.Control name='username' type="text" placeholder="Enter name" onChange={onValueChange}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Control name='UserEmail' type="email" placeholder="Enter email" onChange={onValueChange}/>
                </Form.Group>

                <Button variant="primary" type="submit" onClick={(e)=>sendData(e)}>
                    Submit
                </Button>
            </Form>
        </div>
    );
};
export default PostData;

