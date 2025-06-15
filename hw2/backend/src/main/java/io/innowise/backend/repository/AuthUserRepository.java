package io.innowise.backend.repository;

import io.innowise.backend.entity.AuthUser;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface AuthUserRepository extends JpaRepository<AuthUser, Long> {

    /**
     * Finds an authentication user by their email address.
     *
     * @param email The email to search for.
     * @return An Optional containing the AuthUser if found.
     */
    Optional<AuthUser> findByEmail(String email);
}
