import React from 'react';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';

export class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            activeNav: "Home"
        }
    }

    render() {
        return <Container className="fluid mx-0 px-0"> 
            <Navbar bg="dark" variant="dark" expand="lg" className="fluid my-0">
            <Navbar.Brand href="#home">
            <img
                src="/pixel-butterfly.jpg"
                width="40"
                height="40"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
            />
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="#plays">Plays</Nav.Link>
                <Nav.Link href="#members">Members</Nav.Link>
                <Nav.Link href="#contact">Contact</Nav.Link>
                <Nav.Link href="#about">About</Nav.Link>
            </Nav>
            <Form inline>
                <FormControl type="text" placeholder="Search" className=" mr-sm-2" />
                <Button type="submit">Submit</Button>
            </Form>
            </Navbar.Collapse>
        </Navbar>
      </Container>
    }
    
}