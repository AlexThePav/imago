import React from 'react';

export class PlayForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            title: '', 
            description: ''
        };

        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name

        this.setState({
            [name]: value
        });
    }

    handleSubmit(event) {
        console.log("Submitted:")
        console.log(this.state.title)
        console.log(this.state.description)
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>

                <div className="form-group">
                    <label htmlFor="playTitle">
                        Title:
                        <input 
                            name="title"
                            id="playTitle"
                            type="text"
                            className="form-control" 
                            value={this.state.title} 
                            onChange={this.handleInputChange} />
                    </label>
                </div>

                <div className="form-group">
                    <label htmlFor="playDescription">
                        Description:
                        <textarea
                            name="description"
                            id="playDescription"
                            className="form-control" 
                            value={this.state.description} 
                            onChange={this.handleInputChange} />
                    </label>
                </div>
                    
                <div className="form-group">
                    Cast:
                    <div className="form-check">
                        <input className="form-check-input"
                                type="checkbox"
                                value=""
                                id="member1"/>
                        <label className="form-check-label"
                                htmlFor="member1">
                            Member One
                        </label>
                    </div>
                </div>

                <input 
                    type="submit" 
                    value="Submit" 
                />
            </form>
        );
    }
}