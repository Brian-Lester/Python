from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']



    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,created_at,updated_at,dojo_id) VALUES (%(first_name)s,%(last_name)s,NOW(),NOW(),%(dojo_id)s)"
        return connectToMySQL('dojos_ninjas_schema').query_db(query,data)
    
    @classmethod
    def get_by_dojo_id(cls,data):
        query =' SELECT * from ninjas where dojo_id = %(id)s'
        ninjas=[]
        results =connectToMySQL('dojos_ninjas_schema').query_db(query,data)
        for n in results:
            ninjas.append(cls(n))
        return ninjas
    
    @classmethod
    def get_by_id(cls,data):
        query =' SELECT * from ninjas where id = %(id)s'
        ninjas=[]
        results =connectToMySQL('dojos_ninjas_schema').query_db(query,data)
        for n in results:
            ninjas.append(cls(n))
        return ninjas

    @classmethod
    def save_update(cls,data):
        query = "UPDATE ninjas SET first_name =%(fname)s , last_name=%(lname)s,  dojo_id = %(dojo_id)s,updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL('dojos_ninjas_schema').query_db( query, data )

    @classmethod 
    def delete(cls,data):
        query =' DELETE FROM ninjas where id = %(id)s'
        results= connectToMySQL('dojos_ninjas_schema').query_db( query, data )
        return data
        