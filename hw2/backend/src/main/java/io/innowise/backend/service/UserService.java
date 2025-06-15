package io.innowise.backend.service;

import io.innowise.backend.dto.CreateUserDto;
import io.innowise.backend.dto.UserDto;

import java.util.List;
import java.util.Optional;

public interface UserService {
    List<UserDto> findAll();
    Optional<UserDto> findById(Long id);
    UserDto save(CreateUserDto createUserDto);
    Optional<UserDto> update(Long id, UserDto userDto);
    boolean deleteById(Long id);
}
