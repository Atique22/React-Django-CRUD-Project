import React, { useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function PostData() {

    const [studName, setStudName] = useState('');
    const [studEmail, setStudEmail] = useState('');

    const sendData = async (event) => {
        event.preventDefault();
        console.log(studName);
        console.log(studEmail);
        if (!studName || !studEmail) {
            console.log('Please enter student name and age');
            return;
        }
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/student/', {
                    studName,
                    studEmail
                });
                console.log("data send"+response.data);
            } catch (error) {
                console.error(error);
            }
    };


    return (
        <div className='container col-sm-6 m-5'>
            <Form>
                <Form.Group className="mb-3" controlId="formBasicName">
                    <Form.Control name='studName' type="text" placeholder="Enter name" value={studName}
                        onChange={(event) => setStudName(event.target.value)} />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Control name='studEmail' type="email" placeholder="Enter email" value={studEmail}
                        onChange={(event) => setStudEmail(event.target.value)} />
                </Form.Group>

                <Button variant="primary" type="submit" onClick={(e) => sendData(e)}>
                    Submit
                </Button>
            </Form>
        </div>
    );
};
export default PostData;

