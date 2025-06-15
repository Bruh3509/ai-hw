package io.innowise.backend.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Represents a user record in the main 'users' table.
 * Contains all the publicly visible user information as per the JSONPlaceholder model.
 */
@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    @Column(unique = true)
    private String username;

    @Column(unique = true)
    private String email;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "street", column = @Column(name = "address_street")),
            @AttributeOverride(name = "suite", column = @Column(name = "address_suite")),
            @AttributeOverride(name = "city", column = @Column(name = "address_city")),
            @AttributeOverride(name = "zipcode", column = @Column(name = "address_zipcode"))
    })
    private Address address;

    private String phone;
    private String website;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "name", column = @Column(name = "company_name")),
            @AttributeOverride(name = "catchPhrase", column = @Column(name = "company_catch_phrase")),
            @AttributeOverride(name = "bs", column = @Column(name = "company_bs"))
    })
    private Company company;
}
